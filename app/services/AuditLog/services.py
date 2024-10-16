from datetime import datetime, timedelta, timezone
from fastapi.responses import JSONResponse
from utils.database import create_connection

def get_all_log():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT audit.*, users.*
            FROM audit_log as audit
            INNER JOIN users ON audit.user_id = users.id
            ORDER BY audit.timestamp desc
            """
        )
        temp_data = cursor.fetchall()
        data = []
        
        # Append Data
        for log in temp_data:
            data.append({
                "username": log[6],
                "time": log[1],
                "action": log[2],
                "action_detail": log[3],
                "entity": log[4],
                "roles": log[9],
            })
        return JSONResponse({"data": data}, status_code=200)
    except Exception as e:
        return JSONResponse({"message": "Error while fetch data", "error": e}, status_code=400)

def get_log_by_id(user_id: str):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT audit.*, users.*
            FROM audit_log as audit
            INNER JOIN users ON audit.user_id = users.id
            WHERE user_id=%s
            ORDER BY audit.timestamp desc
            """, (user_id,)
        )
        # Append Data
        temp_data = cursor.fetchall()
        data = []
        for log in temp_data:
            data.append({
                "username": log[6],
                "time": log[1],
                "action": log[2],
                "action_detail": log[3],
                "entity": log[4],
                "roles": log[9]
            })
        return JSONResponse({"data": data}, status_code=200)
    except Exception as e:
        return JSONResponse({"message": "Error while fetch data", "error": e}, status_code=400)

def add_log(id: str, action_type: str, action_detail: str, entity_name: str):
    conn = create_connection()
    cursor = conn.cursor()
    
    # Set Timezone to Local
    offset = timedelta(hours=7)
    local_timezone = timezone(offset)
    now_utc = datetime.now(timezone.utc)
    now = now_utc.astimezone(local_timezone)
    timestamp = now.strftime('%I:%M%p %m/%d/%Y').lstrip('0')
    
    try:
        cursor.execute(
            """
            INSERT INTO audit_log (user_id, timestamp, action_type, action_detail, entity_name)
            VALUES(%s, %s, %s, %s, %s)
            """, (id, timestamp, action_type, action_detail, entity_name)
        )
        conn.commit()
    except Exception as err:
        conn.rollback()
        print(f"Error while adding log: {err}")  # Or log this error to a file or logging service
        raise  # Re-raise the exception to handle it upstream if needed
    finally:
        conn.close()

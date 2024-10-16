import uuid

from utils.database import create_connection
from fastapi.responses import JSONResponse
from services.AuditLog.services import add_log
from utils.utils import decode_jwt

def add_product(request, project_id, project_name, user_token, pm_id, cm_id, sla_id, implementation_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO product(
                product_id, project_id, preventive_maintenance, corrective_maintenance,
                principal_id, product_name, product_category, serial_number, si_number,
                quantity, start_date, end_date, sla_id, implementation_id 
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (str(uuid.uuid4()), project_id, pm_id, cm_id, request.principal_id, request.product_name, 
                  request.product_category, request.serial_number, request.si_number, request.quantity, request.start_date,
                  request.end_date, sla_id, implementation_id)
        )
        conn.commit()
        conn.close()
        user_id = decode_jwt(user_token)
        add_log(user_id, action_type="POST", action_detail="Added a new product '" + request.product_name + "' under the project '" + project_name + "'", entity_name="Product")
        return JSONResponse({"message": "Successful add new data"}, status_code=201)
    except Exception as err:
        return JSONResponse({"messsage": "Error while adding data product", "error": err}, status_code=500)
    
def edit_product(request, product_id, user_token):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            UPDATE product
            SET principal_id=%s, product_name=%s, product_category=%s,
                serial_number=%s, si_number=%s, quantity=%s, start_date=%s, end_date=%s
            WHERE product_id=%s
            """, (request.principal_id, request.product_name, request.product_category,
                request.serial_number, request.si_number, request.quantity,
                request.start_date, request.end_date, product_id)
        )
        conn.commit()
        conn.close()
        user_id = decode_jwt(user_token)
        add_log(user_id, action_type="UPDATE", action_detail="Edited a product '" + request.product_name + "'", entity_name="Product")
        return JSONResponse({"message": f"Successfully updated {request.product_name} in project"}, status_code=200)
    except Exception as err:
        return JSONResponse({"message": "Error while updating data in project", "error": str(err)}, status_code=500)

def delete_product(id, user_token):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            DELETE FROM product 
            WHERE product_id=%s 
            """,(id,)
        )
        conn.commit()
        conn.close()
        user_id = decode_jwt(user_token)
        add_log(user_id, action_type="DELETE", action_detail="Deleted a product", entity_name="Product")
        return JSONResponse({"message": "Delete successfull"}, status_code=200)
    except Exception as err:
        return JSONResponse({"message": "Failed when delete this product", "error": str(err)}, status_code=500)
    
from datetime import datetime
from fastapi.responses import JSONResponse

def get_all_product():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT project.project_id,
                customer.customer_name,
                project.project_name,
                users.username,
                product.product_name,
                product.end_date
            FROM project
            INNER JOIN customer ON project.customer_id = customer.customer_id
            INNER JOIN users ON project.sales_person = users.id
            LEFT JOIN product ON project.project_id = product.project_id
            WHERE project.status='Approved'
            """
        )
        data = []
        temp_data = cursor.fetchall()
        current_date = datetime.now().date()
        for product in temp_data:
            end_date = product[5]
            remaining_days = (end_date - current_date).days if end_date else None
            status = "Ongoing" if remaining_days and remaining_days > 0 else "Expired"
            data.append({
                "project_id": product[0],
                "customer_name": product[1],
                "project_name": product[2],
                "sales_person": product[3],
                "product_name": product[4],
                "remaining_date": f"{remaining_days} days" if remaining_days is not None else "N/A",
                "status": status,
            })
        return JSONResponse({"data": data}, status_code=200)
    except Exception as err:
        return JSONResponse({"message": "Failed to get products", "error": str(err)}, status_code=500)

import uuid
import datetime
from utils.database import create_connection
from utils.utils import check_is_user_sales
from fastapi.responses import JSONResponse
from utils.utils import check_is_user_sales

def get_total_customer():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT COUNT(DISTINCT customer_name) FROM customer"
        )
        temp_data = cursor.fetchone()
        total_customer = temp_data[0]
        return JSONResponse({"data": total_customer}, status_code=200)
    except Exception as err:
        return JSONResponse({"message": "Error count data", "err": str(err)}, status_code=500)

def get_project(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    sales_verify = check_is_user_sales(user_id)
    try:
        if sales_verify:
            cursor.execute(
                "SELECT COUNT(DISTINCT project_id) FROM project WHERE sales_person = %s AND status != 'Draft'", (user_id,)
            )
        else:    
            cursor.execute(
                "SELECT COUNT(DISTINCT project_id) FROM project"
            )
        temp_data = cursor.fetchone()
        total_project = temp_data[0]
        return JSONResponse({"data": total_project}, status_code=200)
    except Exception as err:
        return JSONResponse({"message": "Error count data", "err": str(err)}, status_code=500)

def get_pending_project(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    verify_sales = check_is_user_sales(user_id)
    try:
        if verify_sales:
            cursor.execute(
                """
                SELECT COUNT(*) 
                FROM project 
                WHERE status='Pending' AND sales_person=%s
                """,(user_id,)
            )
        else:
            cursor.execute(
                """
                SELECT COUNT(*) FROM project WHERE status='Pending'
                """
            )
        temp_data = cursor.fetchone()
        total_project = temp_data[0]
        return JSONResponse({"data": total_project}, status_code=200)
    except Exception as err:
        return JSONResponse({"message": "Error count data", "err": str(err)}, status_code=500)

def get_total_created_project(user):
    conn = create_connection()
    cursor = conn.cursor()
    is_sales = check_is_user_sales(user)
    try:
        if not is_sales:
            cursor.execute(
                "SELECT COUNT(project_id) FROM project WHERE created_by=%s", (user,)
            )
            temp_data = cursor.fetchone()
            total_project = temp_data[0]
            return JSONResponse({"data": total_project}, status_code=200)
        else:
            cursor.execute(
                "SELECT COUNT(project_id) FROM project WHERE sales_person=%s AND status != 'Draft'", 
                (user,)
            )
            temp_data = cursor.fetchone()
            total_project = temp_data[0]
            return JSONResponse({"data": total_project}, status_code=200)
    except Exception as err:
        return JSONResponse({"message": "Error count data", "err": str(err)}, status_code=500)

def get_top_customer_project():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT customer.customer_name, COUNT(project.project_id) AS total_project
            FROM customer
            LEFT JOIN project ON customer.customer_id=project.customer_id
            GROUP BY customer.customer_id, customer.customer_name
            ORDER BY total_project DESC
            LIMIT 5
            """
        )
        temp_data = cursor.fetchall()
        labels = []
        total = []
        for data in temp_data:
            labels.append(data[0])
            total.append(data[1])
        data = {
            "labels": labels,
            "totals": total
        }
        return JSONResponse({"data": data}, status_code=200)
    except Exception as err:
        return JSONResponse({"message": "Error count data", "err": str(err)}, status_code=500)

def get_project_by_sales(user):
    conn = create_connection()
    cursor = conn.cursor()
    is_sales = check_is_user_sales(user)
    try:
        if not is_sales:
            cursor.execute(
                """
                SELECT project.project_id, project.project_name, customer.customer_name 
                FROM project
                INNER JOIN customer ON project.customer_id=customer.customer_id
                WHERE created_by=%s
                ORDER BY project.created_at DESC
                LIMIT 5
                """, (user,)
            )
            temp_data = cursor.fetchall()
            data = []
            for project in temp_data:
                data.append({
                    "project_id": project[0],
                    "project_name": project[1],
                    "customer_name": project[2],
                })
            return JSONResponse({"data": data}, status_code=200)
        else: 
            cursor.execute(
                """
                SELECT project.project_id, project.project_name, customer.customer_name 
                FROM project
                INNER JOIN customer ON project.customer_id=customer.customer_id
                WHERE sales_person=%s AND project.status != 'Draft'
                ORDER BY project.created_at DESC
                LIMIT 5
                """, (user,)
            )
            temp_data = cursor.fetchall()
            data = []
            for project in temp_data:
                data.append({
                    "project_id": project[0],
                    "project_name": project[1],
                    "customer_name": project[2],
                })
            return JSONResponse({"data": data}, status_code=200)
    except Exception as err:
        return JSONResponse({"message": "Error count data", "err": str(err)}, status_code=500)

def get_user_total_project(user):
    conn = create_connection()
    cursor = conn.cursor()
    data = []
    try:
        cursor.execute(
            """
            SELECT COUNT(DISTINCT project_id)
            FROM project
            WHERE sales_person=%s AND status='Approved'
            """, (user,)
        )
        temp_data = cursor.fetchone()
        total_customer = temp_data[0]
        try:
            cursor.execute(
                """
                SELECT project_id, project_name 
                FROM project
                WHERE sales_person=%s 
                """, (user,)
            )
            temp_data = cursor.fetchall()
            for project in temp_data:
                data.append({
                    "project_id": project[0],
                    "project_name": project[1]
                })
        except Exception as err:
            return JSONResponse({"message": "Error fetch data", "err": str(err)}, status_code=500)
        
        return JSONResponse({"total": total_customer, "data": data}, status_code=200)
    except Exception as err:
        return JSONResponse({"message": "Error count data", "err": str(err)}, status_code=500)

def get_running_project(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    sales_verify = check_is_user_sales(user_id)
    data = {
        "Contract Finished": 0,
        "<1 year": 0,
        "1+ year": 0,
        "2+ year": 0
    }
    try:
        if sales_verify:
            cursor.execute(
                """
                SELECT start_date, end_date
                FROM project
                WHERE sales_person=%s
                """, (user_id,)
            )
        else:
            cursor.execute(
                """
                SELECT start_date, end_date
                FROM project
                """
            )
        temp_data = cursor.fetchall()
        for row in temp_data:
            diff = datetime.date.today() - row[1]
            days_difference = diff.days
            days_to_year = (days_difference * -1) / 365
            if days_to_year < 1 and days_to_year > 0:
                data["<1 year"] += 1
            elif days_to_year > 1 and days_to_year < 2:
                data["1+ year"] += 1
            elif days_to_year > 2:
                data["2+ year"] += 1
            elif days_to_year < 0:
                data['Contract Finished'] += 1
        return JSONResponse({"data": data}, status_code=200)
    except Exception as err:
        return JSONResponse({"message": "Error diffing data", "err": str(err)}, status_code=500)

def get_dashboard_diff(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    sales_verify = check_is_user_sales(user_id)
    
    # Get current month and previous month
    current_month = datetime.datetime.now().month
    previous_month = current_month - 1 if current_month != 1 else 12
    current_year = datetime.datetime.now().year
    previous_year = current_year if current_month != 1 else current_year - 1 
    
    # Variable Data
    project_diff = 0
    try:
        if sales_verify:
            cursor.execute(
                """
                SELECT 
                    SUM(CASE WHEN EXTRACT(MONTH FROM created_at) = %s AND EXTRACT(YEAR FROM created_at) = %s THEN 1 ELSE 0 END) AS current_month_count,
                    SUM(CASE WHEN EXTRACT(MONTH FROM created_at) = %s AND EXTRACT(YEAR FROM created_at) = %s THEN 1 ELSE 0 END) AS previous_month_count
                FROM project
                WHERE sales_person=%s
                """, (current_month, current_year, previous_month, previous_year, user_id)
            )
        else:
            cursor.execute(
                """
                SELECT 
                    SUM(CASE WHEN EXTRACT(MONTH FROM created_at) = %s AND EXTRACT(YEAR FROM created_at) = %s THEN 1 ELSE 0 END) AS current_month_count,
                    SUM(CASE WHEN EXTRACT(MONTH FROM created_at) = %s AND EXTRACT(YEAR FROM created_at) = %s THEN 1 ELSE 0 END) AS previous_month_count
                FROM project
                """, (current_month, current_year, previous_month, previous_year)
            )            
        row = cursor.fetchone()
        project_diff = row[0] - row[1]
        return JSONResponse({"project_diff": project_diff}, status_code=200)
    except Exception as err:
        return JSONResponse({"message": "Error diffing data", "err": str(err)}, status_code=500)

def get_total_approve(user):
    conn = create_connection()
    cursor = conn.cursor()
    data = []
    try:
        cursor.execute(
            """
            SELECT COUNT(DISTINCT project_id)
            FROM project
            WHERE approved_by=%s
            """, (user,)
        )
        temp_data = cursor.fetchone()
        approved_projects = temp_data[0]
        try:
            cursor.execute(
                """
                SELECT project_id, project_name 
                FROM project
                WHERE approved_by=%s 
                """, (user,)
            )
            temp_data = cursor.fetchall()
            for project in temp_data:
                data.append({
                    "project_id": project[0],
                    "project_name": project[1]
                })
        except Exception as err:
            return JSONResponse({"message": "Error fetch data", "err": str(err)}, status_code=500)
        
        return JSONResponse({"total": approved_projects, "data": data}, status_code=200)
    except Exception as err:
        return JSONResponse({"message": "Error count data", "err": str(err)}, status_code=500)
import argparse
import datetime
import os
import pandas as pd

def create_application(company_name, manual_date, resume, cover, notes):
    today_date = datetime.datetime.now().strftime('%Y-%m-%d')

    if manual_date:
        application_date = input("Enter the application date (YYYY-MM-DD): ")
    else:
        application_date = today_date

    file_name = f"{company_name}_application.txt"

    with open(file_name, 'w') as f:
        f.write(f"Company: {company_name}\n")
        f.write(f"Application Date: {application_date}\n")
        if resume:
            f.write(f"Resume attached: {resume}\n")
        if cover:
            f.write(f"Cover Letter attached: {cover}\n")
        if notes:
            f.write(f"Notes: {notes}\n")

    print(f"Application details saved in {file_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a job application record")
    parser.add_argument("company_name", type=str, help="Company name")
    parser.add_argument("-m", "--manual-date", action="store_true", help="Manually enter the application date")
    parser.add_argument("-r", "--resume", type=str, help="Resume file")
    parser.add_argument("-cl", "--cover", type=str, help="Cover letter file")
    parser.add_argument("--notes", type=str, help="Notes file")

    args = parser.parse_args()

    create_application(args.company_name, args.manual_date, args.resume, args.cover, args.notes)

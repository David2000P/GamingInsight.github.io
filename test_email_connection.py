import smtplib

try:
    server = smtplib.SMTP('smtp.googlemail.com', 587)
    server.starttls()
    server.login('sercanp76@gmail.com', 'urrv qcao vkfz qjdk')
    print("Login successful")
    server.quit()
except Exception as e:
    print(f"Failed to connect: {e}")

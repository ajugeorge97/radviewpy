from radviewclient import RadViewClient

if __name__ == "__main__":
    client = RadViewClient("http://10.67.150.72:5173/")
    client.login("admin", "change-me-now")
    print("Logged in successfully!")
    
    subject = client.orthanc.subjects
    client.logout()

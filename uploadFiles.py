import dropbox
import os

class TransferData ():
    def __init__(self,access_token):
        self.access_token = access_token
    def uploadFiles(self,source,destination):
        drop = dropbox.Dropbox(self.access_token)
        with open(local_path,'rb') as f:
            drop.files_upload(f.read(), dropbox_path , mode = WriteMode('overwrite'))
        for root,dirs,files in os.walk(source):
            relative_path = os.path.relpath(local_path,source)
            dropbox_path = os.path.join(destination,relative_path)
def main():
    access_token = 'sl.A96ZxuAGWcQPCD_OyOHEguPIhKpVE3akbyw8z_5CFCjU_p11mlPIoOIR0QvXLjkcISu1d5qsVFXXxkZ443jLy-OfHX4vRA_K9J4Vu-QBDoQlmQT4OcP3cI9gSl2SITYd9Hg9ibgwQZF8'
    source = input("Enter the file name you want to upload :- ")
    destination = input("Enter the destination of your file :- ")
    newUser.uploadFiles(source,destination)
    print("File has been successfully uploaded !!")
main()
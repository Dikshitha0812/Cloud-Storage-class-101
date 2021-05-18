from os import access
import dropbox
class TransferData:
    def __init__(self,token):
       self.token=token
    def upload_file(self,file_from ,file_to):
        dbx=dropbox.Dropbox(self.token)
        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)
        print("Successfully uploaded the file!!")

def main():
    token='*************'
    transferData=TransferData(token)

    file_from= 'sample.txt'
    file_to='/uploaditsample.txt'

    transferData.upload_file(file_from,file_to)

if __name__ =='__main__':
    main()

from GithubUpload import githubUpload
from DingRobot import dingRobot
from Proxies import proxies
if __name__ == '__main__':
    fdata = githubUpload.read_dir()
    imageUploadData = githubUpload.upload_file(fdata,proxie=proxies.proxie)
    imageUploadUrl = imageUploadData['content']['html_url']
    print(imageUploadUrl)
    dingData = dingRobot.putImageDingDing(imageUploadUrl,"proxiesUrl")
    print(dingData.text)
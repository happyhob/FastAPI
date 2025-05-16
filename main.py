
#pip install -t dependencies -r requirements.txt
'''
✅ 전체 명령어 의미:
requirements.txt에 있는 패키지들을 설치하되, 설치 위치는 dependencies 폴더로 지정하라는 뜻입니다.

📦 예시 시나리오:
서버나 AWS Lambda 같은 환경에서는 시스템 전체에 설치하면 안 되거나, zip 패키징이 필요한 경우가 있음

이럴 때 dependencies 폴더 안에만 설치하면, 그 폴더만 압축하거나 복사해서 사용 가능

fastApi 애플리 케이션에 설치한 모든 종속성이 인슨 새 종족성 디렉토리가 생기고,
이것을 main.py파일과 함께 번들로 묶어
AWS Lambda를 추가해야한다.

'''

#"C:\Program Files\7-Zip\7z.exe" a ..\aws_lambda_artifact.zip * -r
'''
window 환경에서 zip을 사용하는 방법
https://www.7-zip.org/
'''


from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get("/")
async def hello():
    return {"message": "Hello My name is hobin"}
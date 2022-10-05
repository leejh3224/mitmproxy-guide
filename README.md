# Mitmproxy Guide

Mimproxy 설치 및 연동을 위한 스크립트가 있는 저장소입니다.

## Mitmproxy 설치 및 설정

> 주의) 아래 스크립트는 맥 환경에서만 실행 가능합니다.

```bash
python3 setup.py
```

위 스크립트를 실행시키면 mitmproxy를 설치하고 설정 파일을 생성합니다.

스크립트 실행 완료 후 mitmweb 명령어를 실행하여 프록시 디버거를 실행시킵니다.

```bash
mitmweb
```

## 디바이스 설정 방법

mitmproxy 설치가 완료되었다면, 앱이 설치된 디바이스에 디버깅을 위한 설정을 해줘야합니다.

해당 설정을 위한 가이드를 확인하려면 

```bash
# for iOS
python3 help.py

# for AOS
python3 help.py -p AOS
```

위 명령어를 실행합니다.

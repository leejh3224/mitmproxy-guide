import argparse
import subprocess
import sys

import const


def _help():
    parser = argparse.ArgumentParser()
    parser.add_argument('--platform', '-p',
                        choices=["iOS", "AOS"],
                        default="iOS",
                        help="display proxy debugging setup guide for given platform")

    args = parser.parse_args()
    platform = args.platform

    print(f"<{platform} 프록시 디버깅 설정 방법>")
    print("먼저 다음 명령어를 실행하여 proxy 서버를 띄웁니다: `mitmweb`\n")

    print("# 네트워크 프록시 구성")
    print("1. 앱이 설치된 디바이스와 맥이 Wi-Fi 같은 네트워크에 연결되어 있는지 확인합니다.")

    ipaddress = subprocess.check_output(["ipconfig", "getifaddr", "en0"], stderr=subprocess.STDOUT) \
        .decode(sys.stdout.encoding) \
        .replace("\n", "")

    if platform == "iOS":
        print("2. 디바이스의 [설정] > [Wi-Fi]로 간 뒤, 연결된 네트워크를 눌러 상세로 진입합니다.")
        print(f"3. HTTP 프록시 > 프록시 구성 > 수동을 선택한 뒤, 서버에 {ipaddress}, 포트에 {const.proxy_port}를 입력합니다. (인증은 꺼진 그대로 둡니다.)")

        print("3-1. iOS 시뮬레이터를 사용 중인 경우 아래 명령어를 실행하여 맥에서 사용 중인 Wi-Fi 네트워크에 프록시 설정을 활성화합니다.")
        print(f"networksetup -setwebproxy wi-fi localhost {const.proxy_port} && networksetup -setsecurewebproxy wi-fi localhost {const.proxy_port}\n")
        
        print("# CA 인증서 설치 및 신뢰하기")
        print("4. 인증서 설치를 위해 사파리를 켠 뒤, `mitm.it`로 이동합니다.")
        print("5. iOS 메뉴 아래의 Get mitmproxy-ca-cert.pem 버튼을 눌러 프로파일을 설치합니다.")
        print("6. [설정] > [프로파일이 다운로드됨]으로 이동하여 프로파일을 설치해줍니다.")
        print("7. 프로파일 설치가 완료되었다면 [설정] > [일반] > [정보] > [인증서 신뢰 설정]으로 이동한 뒤 [루트 인증서 전체 신뢰 활성화] 항목 아래의 mitmproxy를 활성화합니다.\n")

    if platform == "AOS":
        print("2. 디바이스의 [설정] > [연결] > [Wi-Fi]로 간 뒤, 연결된 네트워크를 선택하고 더보기를 눌러 [프록시]를 선택합니다.")
        print(f"3. [프록시]에서 수동을 선택하고, [프록시 호스트 이름]에 {ipaddress}, [프록시 포트]에 {const.proxy_port}를 입력합니다. (프록시 예외 대상은 따로 설정하지 않습니다.)")
        print("3-1. AOS 에뮬레이터를 사용 중일 경우 https://developer.android.com/studio/run/emulator-networking#proxy를 참고하여 프록시를 설정합니다.")
        print("3-2. AOS 에뮬레이터에 proxy 메뉴가 보이지 않는 경우, Android Studio > Preferences > Tools > Emulator > Launch in a tool window를 체크 해제하고 IDE를 재시작합니다.\n")

        print("# CA 인증서 설치 및 신뢰하기")
        print("4. 인증서 설치를 위해 크롬을 켠 뒤, `mitm.it`로 이동합니다.")
        print("5. Android 메뉴 아래의 Get mitmproxy-ca-cert.cer 버튼을 눌러 인증서 파일을 설치합니다.")
        print("6. 인증서를 설치할 수 없다는 팝업이 뜰텐데 확인을 눌러줍니다.")
        print("7. [설정] > [생체 인식 및 보안] > [기타 보안 설정] > [기기에 저장된 인증서 설치] > [CA 인증서]를 선택한 뒤, Download에 있는 mitmproxy-ca-cert.cer.crt 파일을 선택하여 인증서를 설치합니다.")
        print("7-1. 언어가 영어로 설정되어 있을 경우 [Settings] > [Security] > [More security settings] > [Encryption & credentials] > [Install a certificate] > [CA certificate]를 선택한 뒤, Download에 있는 mitmproxy-ca-cert.cer.crt 파일을 선택하여 인증서를 설치합니다.\n")

    print("모든 설정이 완료되었습니다. 이제 앱을 실행하면 `http://127.0.0.1:8002/#/flows`에 트래픽이 표시됩니다.")
    print("만약 디버깅이 완료되었다면 프록시 설정을 해제합니다.\n")
    print("iOS 시뮬레이터를 사용 중인 경우, 프록시 설정 해제를 위해 아래 명령어를 실행합니다.")
    print("networksetup -setwebproxystate wi-fi off")

if __name__ == "__main__":
    _help()

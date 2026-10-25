# 검증 기록

검사일: 2026-10-25. 대상: YunSangYeong/Engineer-Architectural-Work-CBT.

## 근거와 콘텐츠 검토

최신 표준 v1.4.0의 전체 폴더는 76b990b8720adfa85c22a0a8f699b17094aa357b에서 읽고 복사했다. 기준 앱은 b9a682ccff1b460334b78d5bfad9375b7ec4fbb6에서 git archive로 읽기용 추출 후 실제 코드를 재사용했다. 원본 .git, 문항 JSON, 생성 원고, 개인 데이터 및 원본 배포 기록은 가져오지 않았다. 원본 라이선스의 저작권 표기를 보존했다.

Q-Net 요청: `https://www.q-net.or.kr/crf005.do?id=crf00503&jmCd=1630`.
실제 오류: `URLError <urlopen error Tunnel connection failed: 403 Forbidden>`.
공식 원문 확인 실패를 숨기지 않는다. 적용 시험 규칙은 README와 qualification.ts의 잠정 값이며 현행 공식 규칙 확인 완료가 아니다. 공식 기출 원문·정답·회차·재배포 조건을 확보하지 않아 기출은 수록하지 않았다. 법령 원문은 확보하지 않았으며 법규에는 현행 수치 조항을 넣지 않았다.

원고 scripts/concepts.txt는 과목별 20개로 구성했다. 개념 문장과 오답 보기를 작성하면서 단일 정답성과 적용 조건을 내부 검토했다. 법규는 기초 용어·법령 검토 방법 중심으로 제한했다. 개념형의 다른 보기들이 문맥상 동치 정답인지 템플릿 단위로 검토했다. 외부 문헌 대조나 전문가 검수 및 전 문장의 독립 검토를 수행한 것은 아니다.

계산 템플릿은 다음과 같다. 독립 테스트는 Python 생성식을 import하지 않는다.

| 과목 | family | 내부 검토한 조건·단위 |
| --- | --- | --- |
| 시공 | concreteVolume | 직육면체 순체적, m³, 손실·철근 공제 제외 |
| 시공 | tileCount | 바닥면적/장당면적, 정수 장, 줄눈·절단·손실 제외 |
| 시공 | laborHours | 작업량/생산성, 인·h, 인원 수와 소요시간을 구별 |
| 구조 | axialStress | 중심 인장 평균응력, kN→N, N/mm²=MPa, 소수 둘째 자리 |
| 구조 | beamMoment | 단순보 전 구간 등분포하중, 중앙 반력·모멘트 평형으로 독립 검산 |
| 구조 | beamReaction | 중앙 집중하중 단순보, 모멘트 평형으로 반력 검산 |
| 설비 | sensibleHeat | 정상 상태 Q=UAΔT, W, 열교·일사 제외 |
| 설비 | waterFlow | 명시적 동시 사용, 개별 유량 합산, L/min |
| 설비 | lightingFlux | 작업면 입사 광속=조도×면적, lm, 등기구 출력 광속과 구분 |

9유형 각각 100개 조건. 의미상 같은 원리를 쓰는 숫자 변형 900개를 독립 개념으로 세지 않는다. ID 및 정규화 본문·정렬 보기의 중복은 0개다. 계산형 선택지의 숫자 동치와 단위, 정답 번호는 전 900개를 별도 자동 검사한다. 내부 reviewed=1000, pending=0, 제외=0, 기출=0, 복원=0. 외부 전문가 검수/공식 기준 대조 완료=0. 수량 부족=0이지만 과목 분포와 실제 시험 대비 범위는 제한적이다.

## 로컬 검사

작업 디렉터리: `/workspace/Engineer-Architectural-Work-CBT`.

- `npm ci --cache /workspace/.npm-cache`: 종료 0, lockfile 기반 110개 패키지 설치.
- `npm test`: 917개 통과, 종료 0 (계산형 900개의 독립 수치 검증 포함).
- `npm run build`: 타입 검사·Vite 프로덕션 빌드 종료 0. 문제 데이터 포함 JS가 500 kB를 넘어 청크 크기 권고 경고가 있다. 경고를 숨기거나 제한을 완화하지 않았다.
- `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH=/usr/bin/chromium npm run test:e2e`: 최종 28개 통과(데스크톱 14, Pixel 7 에뮬레이션 14), 실패·건너뜀 0, 종료 0. 빌드 포함 39.8초.
- 최초 브라우저 검사 26 통과/2 실패: 상단 안내 검사가 통계의 정상 보관 범위 안내까지 금지한 검사 범위 오류. 금지 대상(비공식·잠정 규칙 상단 배너)으로 바로잡은 뒤 관련 2개 및 최종 전체 28개 통과.
- 390×480·740×360에서 실제 mouse.wheel 및 CDP touchStart/move/end 입력으로 메뉴 하단 백업 다운로드·초기화 창 열기·상단 대시보드 선택을 검증. scrollTop 대입으로 이동하지 않음. 별도 글자 확대 검사 통과.
- 실전 100문항·과목별 응답 12개로 평균 60점 합격, 답안 수정·새로고침·절대 종료 시각·만료 후 재접속·중복 제출 방지, 랜덤·오답·북마크·통계·JSON/CSV 등록·사용자 로컬 승인·초기화·저장 손상 원본 보존·저장 실패 경고·두 모드 Space와 마지막 문제 보호를 브라우저에서 확인.
- 생성 반복 시 기본 JSON과 JSON/CSV 양식이 바이트 단위로 동일함을 확인. 표준 폴더 9개 파일은 최신 main과 바이트 단위 일치.
- `npm run dev -- --port 5173 --strictPort`: 서버 시작 및 별도 Chromium에서 대시보드→랜덤 답안→해설→Space 다음 문제 동작 확인. 종료 0인 스모크 검사, 개발 서버는 실행 중.
- Chromium 데스크톱과 Pixel 7 에뮬레이션을 사용한다. 실제 휴대전화·Safari·Firefox·블로그 iframe 검증은 미실행이다.

## 원격·CI·배포

배포 사전 확인에서 첫 차단이 발생하여 중단했다.

- `git fetch origin main`: 성공. 원격 main은 초기 커밋을 유지한다.
- GH_TOKEN은 set, GITHUB_TOKEN은 unset임을 값 노출 없이 확인했다. 토큰 부재로 추정하지 않았다.
- 최초 API 명령: `gh api repos/YunSangYeong/Engineer-Architectural-Work-CBT --jq '{default_branch,has_pages,permissions}'`.
- 종료 1, 실제 오류: `Get "https://api.github.com/repos/YunSangYeong/Engineer-Architectural-Work-CBT": Forbidden`.
- 현재 네트워크 허용 목록에는 api.github.com이 없다. API 거부 후 curl 등 다른 경로로 접근하지 않았으며, API 조회를 재시도하지 않았다. 토큰 권한과 Pages Source는 API 결과를 받지 못해 확인 불가다.
- **main push, CI, configure-pages, deploy는 실행하지 않았다.** Pages의 기존 게시 여부도 미확인이다. 배포 성공과 공개 화면 확인 모두 미확인이다.
- 배포를 유발하지 않는 `codex/architectural-cbt` 브랜치에 코드 보존만 수행한다. workflow의 push 대상은 main뿐이며 PR도 생성하지 않아 자동 검증·배포를 시작하지 않는다. 원격 보존 커밋은 최종 답변과 Git 이력을 확인한다.
- 첫 차단 이후 workflow 재실행·수동 실행·대체 배포·배포 유발 추가 push를 하지 않는다. 사용자가 이후 직접 마무리하며, 새로운 명시적 요청 없이는 재시도하지 않는다.
- 최초 Pages 설정 또는 승인이 필요한지는 확인하지 못했다. 필요하다고 단정하여 임의 설정을 변경하지 않았다. 기존에 배포된 다른 프로젝트는 변경하거나 재배포하지 않았다.

예정 기본 URL은 https://YunSangYeong.github.io/Engineer-Architectural-Work-CBT/ 이며 실제 게시 주소로 검증한 것은 아니다.

## 재사용 클라우드 설정

설치 스크립트와 시작 지침을 환경 draft에 저장했다. 이는 실행 중 인스턴스의 개발 검증과 별개이며, 새 환경 snapshot 게시나 새 작업에서의 복원을 검증한 것이 아니다. 검토·저장·게시는 환경 설정 UI에서 사용자가 수행한다. API 및 공식 자료 접근에 필요한 도메인 추가도 draft로만 저장하며, 저장만으로 현재 네트워크에 적용되거나 Pages가 배포되는 것은 아니다.

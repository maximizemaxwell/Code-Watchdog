# MacroSense

## Dataset

### Mouse

[Remouse](https://ieee-dataport.org/documents/remouse-mouse-dynamic-dataset)
[Mouse-Dynamics-Challenge](https://github.com/balabit/Mouse-Dynamics-Challenge)


### Keyboard
[KeyRecs](https://zenodo.org/records/7886743)


## Process

### 학습 방법
비지도 학습:
- 일반 사용자 입력 데이터를 기반으로 정상 패턴을 학습하고 매크로 입력을 이상치로 탐지
- Isolation Forest(IF)

이상 점수 계산법: 키보드와 마우스를 개별 점수로 계산 후 평균을 내어 최종 점수로 사용

### 실시간 애플리케이션 테스트
- pynput 라이브러리를 이용해 키보드와 마우스 이벤트를 수집


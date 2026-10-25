"""Deterministic authored bank. No third-party exam text. See docs/verification.md."""
import csv
import json
from decimal import Decimal
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SOURCE='https://github.com/YunSangYeong/Engineer-Architectural-Work-CBT/blob/main/docs/verification.md'
bank=[]
def add(subject,topic,stem,choices,explanation,**extra):
 index=len(bank); shift=index%4
 options=choices[shift:]+choices[:shift]
 bank.append(dict(id=extra.pop('id',f'ARC-C-{index+1:03}'),subject=subject,topic=topic,question=stem,choices=options,answer=options.index(choices[0])+1,explanation=explanation,difficulty='중' if extra else '하',year=None,session=None,type='original',sourceUrl=SOURCE,verificationStatus='reviewed',reviewNote='AI 일반 지식 기반 자체 작성. 템플릿의 조건·문장·단일 정답 내부 검토. 계산형은 별도 TypeScript 수식으로 전 조건 재계산. 외부 문헌 정답 대조·전문가 검수·공식 출제기준 대조 미완료. 법규는 일반 개념·검토 절차만 다루며 현행 조문·수치 규정 확인을 대신하지 않음.',version='architecture-main',rights='자체 제작 · CC BY 4.0 · Engineer-Architectural-Work-CBT contributors',**extra))
subject=''
for line in (ROOT/'scripts/concepts.txt').read_text().splitlines():
 if line.startswith('# '): subject=line[2:]; continue
 if not line: continue
 topic,stem,a,b,c,d,explanation=line.split('|')
 add(subject,topic,stem,[a,b,c,d],explanation)
assert len(bank)==100

def numeric(subject,kind,topic,i,values,result,unit,stem,explanation):
 result=float(result); result=int(result) if result.is_integer() else result
 alternatives=[result,result*2,result*3,result*4]
 def fmt(n): return format(Decimal(str(n)).normalize(),'f')+' '+unit
 add(subject,topic,stem,[fmt(n) for n in alternatives],explanation,id=f'ARC-N-{kind}-{i+1:03}',family=kind,calculation=dict(kind=kind,values=values,result=result,unit=unit))
for i in range(100):
 a=4+i//10; b=5+i%10
 numeric('건축시공','concreteVolume','콘크리트 물량',i,[a,b,0.2],Decimal(a)*Decimal(b)*Decimal('0.2'),'m³',f'가로 {a} m, 세로 {b} m, 두께 0.20 m인 직육면체 콘크리트 슬래브의 순체적은? 개구부·손실·철근 체적은 무시한다.',f'직육면체 순체적 V=가로×세로×두께. 단위는 모두 m이다. {a}×{b}×0.20={Decimal(a)*Decimal(b)*Decimal("0.2")} m³. 타설 할증과 철근 체적 공제는 조건에 따라 적용하지 않는다.')
 numeric('건축시공','tileCount','마감 수량',i,[a,b,0.25],a*b*4,'장',f'가로 {a} m, 세로 {b} m의 바닥에 한 장당 0.25 m²를 덮는 타일을 붙인다. 줄눈·절단·손실을 무시할 때 필요한 타일 수는?',f'바닥 면적 A={a}×{b}={a*b} m². 필요 수량 N=A/장당 면적={a*b}/0.25={a*b*4}장이다. 줄눈과 손실이 없다는 조건이며 실제 발주 수량의 할증은 포함하지 않는다.')
 numeric('건축시공','laborHours','작업 생산성',i,[a*b,2],a*b/2,'인·h',f'작업량이 {a*b} m²이고 생산성이 2 m²/(인·h)인 단일 작업의 필요 인시(人時)는? 대기·휴식·작업 간섭은 무시한다. [조건 코드 L-{i+1:03}]',f'필요 인시=작업량/생산성. {a*b} m² ÷ 2 m²/(인·h)={a*b/2} 인·h이다. 이는 인원과 시간의 곱이며 몇 명이 몇 시간 일할지는 별도 편성 문제다.')
 # unique input pairs (not just unique labels) for labor
 bank[-1]['calculation']['values']=[a,b,2]
 bank[-1]['question']=f'가로 {a} m, 세로 {b} m의 바닥 마감 생산성이 2 m²/(인·h)이다. 대기·휴식·작업 간섭을 무시할 때 필요 인시는?'
 numeric('건축구조','axialStress','축응력',i,[a*10,b*100],a*100/b,'MPa',f'중심축 인장력 {a*10} kN이 단면적 {b*100} mm²인 균일 부재에 작용한다. 응력 집중을 무시한 평균 인장응력은? 소수 둘째 자리까지 표시한 값 중 고르시오.',f'평균 인장응력 σ=N/A. {a*10} kN={a*10000} N이고 1 N/mm²=1 MPa이다. 따라서 {a*10000}/{b*100}={a*100/b:.2f} MPa. 국부 응력 집중은 무시한 평균값이다.')
 # For this family all options use exactly two decimal places; avoid binary format artifacts.
 q=bank[-1]; answer=q['answer']; val=Decimal(a*100)/Decimal(b); val=val.quantize(Decimal('0.01'))
 q['calculation']['result']=float(val);q['calculation']['precision']=2
 opts=[f'{val*k:.2f} MPa' for k in [1,2,3,4]]; shift=(len(bank)-1)%4;q['choices']=opts[shift:]+opts[:shift];q['answer']=q['choices'].index(opts[0])+1
 numeric('건축구조','beamMoment','보 휨모멘트',i,[a,b],a*b*b/8,'kN·m',f'길이 {b} m인 단순지지 보 전 길이에 등분포하중 {a} kN/m가 작용한다. 자중은 하중에 포함되어 있다. 최대 휨모멘트의 크기는?',f'전 구간 등분포하중 단순보의 최대 휨모멘트는 중앙에서 wL²/8이다. {a}×{b}²/8={a*b*b/8} kN·m. 이 식은 주어진 지지와 하중 조건에 한정된다.')
 numeric('건축구조','beamReaction','단순보 반력',i,[a*100+b,b],(a*100+b)/2,'kN',f'길이 {b} m인 단순지지 보 중앙에 집중하중 {a*100+b} kN이 아래로 작용한다. 보 자중을 무시할 때 왼쪽 수직 반력의 크기는?',f'중앙 집중하중과 대칭 지지 조건에서 양쪽 반력은 같다. 수직력 평형 R_A+R_B={a*100+b} kN이고 중앙에 대한 대칭으로 각각 P/2={(a*100+b)/2} kN이다. 길이 {b} m는 반력의 비를 바꾸지 않는다.')
 numeric('건축설비','sensibleHeat','정상 열전달',i,[a,b*10,10],a*b*100,'W',f'열관류율 {a} W/(m²·K), 면적 {b*10} m²인 평면 벽체의 양쪽 온도 차가 10 K이다. 정상 상태이며 열교와 일사 영향이 없을 때 열전달률의 크기는?',f'정상 열전달률 Q=U A ΔT. {a}×{b*10}×10={a*b*100} W. 열관류율에 벽체 양측 표면 열저항을 포함한 값이 주어졌다고 보며 열교와 일사 영향은 제외한다.')
 numeric('건축설비','waterFlow','급수 유량',i,[a,b],a*b,'L/min',f'동시에 사용하는 동일 수전이 {a}개이고 수전 하나의 유량이 {b} L/min이다. 누수와 저장량 변화를 무시할 때 합계 유량은?',f'모든 수전이 동시에 주어진 유량으로 흐르므로 합계 유량 Q=개수×개별 유량={a}×{b}={a*b} L/min이다. 실제 설계의 동시 사용률 추정과 구별한 단순 합산 조건이다.')
 numeric('건축설비','lightingFlux','조도와 광속',i,[a*100,b*10],a*b*1000,'lm',f'면적 {b*10} m²인 작업면 전체에 {a*100} lx의 조도가 균일하게 형성되어 있다. 작업면에 입사하는 총 광속은? 광원의 총 출력 광속이 아니라 작업면 입사 광속을 묻는다.',f'조도 E=입사 광속 Φ/면적 A이며 1 lx=1 lm/m²이다. Φ=E A={a*100}×{b*10}={a*b*1000} lm이다. 조명률과 유지율을 적용한 등기구 선정용 출력 광속은 이 문항의 대상이 아니다.')
# Review duplicate exact normalized wording and options, independent of option order.
def fingerprint(q): return ''.join((q['question']+'|'+ '|'.join(sorted(q['choices']))).split()).casefold()
assert len({q['id'] for q in bank})==len(bank)
assert len({fingerprint(q) for q in bank})==len(bank)
assert len(bank)==1000
(ROOT/'src/data/questions.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2)+'\n')
example={**bank[0], 'id':'LOCAL-EXAMPLE-001', 'verificationStatus':'pending'}
# Keep template in Korean, distinct from the default bank.
example.update(question='등록 양식 예제: 가사 동선 계획에서 우선 검토할 것은?',choices=['공간 사이의 이동 거리와 간섭','벽지 포장지 색만','공사 업체 이름만','가구 상표만'],answer=1,explanation='동선 계획은 이용자의 실제 이동과 공간 사이의 관계를 검토하는 작업이다. 이 등록용 예제는 기본 문제은행과 별개의 문항으로, 이용자가 내용과 출처 및 권리를 확인해야 한다.',reviewNote='직접 작성한 등록 양식 예제. 사용자가 내용·출처·권리를 검토해야 합니다.')
(ROOT/'public/templates/questions.json').write_text(json.dumps([example],ensure_ascii=False,indent=2)+'\n')
fields=[k for k in example if k!='choices']+['choice1','choice2','choice3','choice4']
with (ROOT/'public/templates/questions.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerow({**{k:v for k,v in example.items() if k!='choices'},**{f'choice{i+1}':c for i,c in enumerate(example['choices'])}})
print('Registered',len(bank),'original questions; concepts 100; numeric 900; families 9; years/sessions null.')

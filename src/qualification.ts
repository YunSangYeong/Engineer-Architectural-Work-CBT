// 공식 페이지 접근이 차단되어 원문 대조 전인 학습용 설정. 확인 상태를 숨기지 않는다.
export const QUALIFICATION = {
  name: "건축기사", slug: "architectural-work-cbt", bankId: "architecture-main",
  rulesVerificationStatus: "pending",
  officialSources: ["https://www.q-net.or.kr/crf005.do?id=crf00503&jmCd=1630"],
  subjects: ["건축계획", "건축시공", "건축구조", "건축설비", "건축법규"],
  exam: { questionCount: 100, perSubject: 20, durationMinutes: 150, choiceCount: 4, passScore: 60, subjectCutoff: 40 },
  storageKey: "architectural-work-cbt:v1",
  targetReviewedCount: 1000,
} as const;
export const EXAM = QUALIFICATION.exam;

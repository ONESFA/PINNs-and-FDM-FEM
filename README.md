# PINNs-and-FDM-FEM

2차원 파동방정식 $u_{tt}=c^2(u_{xx}+u_{yy})$ 을 **PINN(Physics-Informed Neural Network)** 과 **FDM(유한차분법)** 으로 풀고,
정확도·에너지 보존·오차 구조를 비교하는 프로젝트입니다.

- 영역: $\Omega=[0,1]^2$, $t\in[0,T]$
- 초기 조건: $u(x,y,0)=\sin\pi x\,\sin\pi y$, $u_t(x,y,0)=0$
- 경계 조건: $\partial\Omega$ 에서 $u=0$ (동차 디리클레)
- 정확해: $u=\sin\pi x\,\sin\pi y\,\cos(\sqrt2\,\pi c\,t)$

## 폴더 구조

```
notebooks/   실험 노트북 (아래 표)
src/pinn/    손실함수 초안 코드 (loss_v1.py, loss_v2.py)
docs/        보고서·정리 문서 (오차분석 보고서 .docx, 손실함수 설명, PINN vs FDM 비교)
docs/archive 주차별 회의 메모
```

## 노트북

| 노트북 | 내용 |
|---|---|
| `PINNS_구현_뼈대.ipynb` | 최초 구현 뼈대 (점 → 신경망 → 손실 → 최적화) |
| `손실함수_구현_가중치 적용 X.ipynb` | 가중치 없는 손실함수 구현 |
| `PINNS_v2.ipynb` | 상대 L2 오차, 재샘플링/Sobol, 가중치(고정·grad-norm), Adam → L-BFGS |
| `PINNS_v2_time_marching.ipynb` | v2 + **PDE 내부 영역 Time-Marching** (`TM_MODE`): 시간 구간 분할 / 인과성 가중치(Causal PINN) / 시간축 적응형 샘플링 |
| `PINNS_v3.ipynb` | Time-Marching + 입력 정규화, hard BC, 초기 기울기 손실, 안정적인 grad-norm, L-BFGS 발산 복원, **에너지·잔차 오차 추정 검증**(보고서 4~5장), **FDM 기준선·수렴 차수·PINN vs FDM 오차 맵**(보고서 7장) |

모든 하이퍼파라미터는 각 노트북의 **0번 설정 셀**에서만 바꿉니다.

## 실행

Colab: 각 노트북 맨 위의 *Open in Colab* 배지를 누르면 됩니다.

로컬:

```bash
pip install -r requirements.txt
jupyter notebook notebooks/PINNS_v3.ipynb
```

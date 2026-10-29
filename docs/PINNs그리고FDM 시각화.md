## 🌊 PINN vs FDM 파이프라인 시각화 비교

두 기법이 편미분방정식(PDE)을 해결하는 관점과 수치해석적 연산 흐름의 차이를 4단계로 비교합니다.

| 비교 단계 (Step) | 🧠 PINN (Physics-Informed Neural Network) | 🧮 FDM (Finite Difference Method) |
|:---|:---|:---|
| **1. 데이터 입력**<br>*(Data Input)* | **무작위 콜로케이션 포인트 샘플링**<br><br>- 내부점, 경계점, 초기점 생성<br>- `(x_f, y_f, t_f)` 무작위 샘플링 | **고정된 시공간 격자 생성**<br><br>- `nx`, `ny`, `nt` 기반 Mesh 생성<br>- `dx`, `dy`, `dt` 설정 및 CFL 조건 확인 |
| **2. 해의 근사**<br>*(Approximation)* | **다층 퍼셉트론(MLP)을 통한 해 근사**<br><br>- 입력: `(t, x, y)`<br>- `Linear` + `Tanh` 레이어 통과<br>- 예측값: \(u_\theta(t,x,y)\) | **격자점별 해의 초기 상태 설정**<br><br>- `u_prev`, `u_curr`, `u_next` 초기화<br>- 초기 조건에 따라 격자점에 초기값 할당 |
| **3. 물리 법칙 적용**<br>*(Equation)* | **자동미분을 통한 PDE 잔차 계산**<br><br>- `torch.autograd.grad`로 미분 계산<br>- PDE 잔차:<br>\(r_\theta = u_{tt} - c^2(u_{xx}+u_{yy})\) | **인접 격자점을 이용한 중앙차분법**<br><br>- 주변 격자점의 값을 이용해 다음 시간 단계 계산<br>- 내부 격자점 업데이트: `u_next[1:-1, 1:-1]` |
| **4. 해 계산 및 전진**<br>*(Solving)* | **역전파 및 신경망 가중치 업데이트**<br><br>- 전체 손실함수:<br>\(L = w_{pde}L_{pde} + w_{bc}L_{bc} + w_{ic}L_{ic}\)<br>- `loss.backward()` 및 `optimizer.step()`<br>- 반복적인 비선형 최적화로 해 근사 | **시간 전진(Time-stepping)**<br><br>- `for n in range(nt):` 반복<br>- 현재 및 이전 시간 단계의 값을 이용해 다음 단계 계산<br>- `u_prev`, `u_curr`, `u_next` 갱신 |

### 핵심 차이

- **PINN:** 신경망의 가중치를 최적화하여 PDE와 초기·경계조건을 만족하는 해를 근사합니다.
- **FDM:** 공간과 시간을 격자로 나누고, 유한차분 근사식을 이용해 각 격자점의 해를 순차적으로 계산합니다.

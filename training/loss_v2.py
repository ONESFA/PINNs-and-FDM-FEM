import torch

# 수정된 학습 루프 (가중치 w_pde, w_bc, w_ic 도입)
def train_step_weighted(model, optimizer, t_col, x_col, y_col, t_bc, x_bc, y_bc, u_bc_true, t_ic, x_ic, y_ic, u_ic_true, c=1.0, w_pde=1.0, w_bc=1.0, w_ic=1.0):
    optimizer.zero_grad()
    
    # 1. PDE Loss 계산 (기존에 정의된 pde_loss 함수 사용)
    loss_pde = pde_loss(model, t_col, x_col, y_col, c)
    
    # 2. Boundary Condition (경계조건) Loss 계산
    u_bc_pred = model(t_bc, x_bc, y_bc)
    loss_bc = torch.mean((u_bc_pred - u_bc_true)**2)
    
    # 3. Initial Condition (초기조건) Loss 계산
    u_ic_pred = model(t_ic, x_ic, y_ic)
    loss_ic = torch.mean((u_ic_pred - u_ic_true)**2)
    
    # 4. 가중치가 적용된 최종 Loss
    total_loss = (w_pde * loss_pde) + (w_bc * loss_bc) + (w_ic * loss_ic)
    
    total_loss.backward()
    optimizer.step()
    
    return total_loss.item(), loss_pde.item(), loss_bc.item(), loss_ic.item()

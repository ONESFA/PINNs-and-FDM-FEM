#기본적 PDE LOSS
def loss_pde(model, x_f, y_f, t_f, c=1.0):

    residual = pde_residual(
        model,
        x_f,
        y_f,
        t_f,
        c
    )

    return torch.mean(residual**2)

#초기 조건 LOSS
def loss_ic(model, x_ic, y_ic, u_ic):

    t_ic = torch.zeros_like(x_ic)

    u_pred = model(
        x_ic,
        y_ic,
        t_ic
    )

    return torch.mean((u_pred - u_ic)**2)

#경계 조건 LOSS
def loss_bc(model, x_bc, y_bc, t_bc):

    u_pred = model(
        x_bc,
        y_bc,
        t_bc
    )

    # u = 0
    return torch.mean(u_pred**2)

#최종 조건 LOSS
def total_loss(
    model,
    x_f, y_f, t_f,
    x_bc, y_bc, t_bc,
    x_ic, y_ic, u_ic,
    v_ic
):

    # PDE
    L_pde = loss_pde(
        model,
        x_f, y_f, t_f
    )

    # Boundary condition
    L_bc = loss_bc(
        model,
        x_bc, y_bc, t_bc
    )

    # Initial displacement
    L_ic = loss_ic(
        model,
        x_ic, y_ic, u_ic
    )

    # Initial velocity
    L_ic_velocity = loss_ic_velocity(
        model,
        x_ic, y_ic, v_ic
    )

    # 기본적인 PINN loss
    loss = (
        L_pde
        + L_bc
        + L_ic
        + L_ic_velocity
    )

    return loss, L_pde, L_bc, L_ic, L_ic_velocity

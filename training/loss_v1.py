def total_loss(
    model,

    x_f, y_f, t_f,

    x_bc, y_bc, t_bc,

    x_ic, y_ic,
    u_ic,
    v_ic,

    c=1.0
):

    # PDE Loss
    L_pde = loss_pde(
        model,
        x_f,
        y_f,
        t_f,
        c
    )

    # Boundary Condition Loss
    L_bc = loss_bc(
        model,
        x_bc,
        y_bc,
        t_bc
    )

    # Initial Displacement Loss
    L_ic = loss_ic(
        model,
        x_ic,
        y_ic,
        u_ic
    )

    # Initial Velocity Loss
    L_ic_velocity = loss_ic_velocity(
        model,
        x_ic,
        y_ic,
        v_ic
    )

    # Total
    loss = (
        L_pde
        + L_bc
        + L_ic
        + L_ic_velocity
    )

    return (
        loss,
        L_pde,
        L_bc,
        L_ic,
        L_ic_velocity
    )


def loss_pde(model, x_f, y_f, t_f, c=1.0):

    residual = pde_residual(
        model,
        x_f,
        y_f,
        t_f,
        c
    )

    return torch.mean(residual**2)

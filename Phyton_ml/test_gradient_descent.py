def gradient_descent(alpha, epochs=10):
    w = 0.0

    print(f"\nLearning rate: {alpha}")

    for epoch in range(epochs):
        loss = (w - 3) ** 2
        gradient = 2 * (w - 3)

        print(
            f"Epoch {epoch + 1:2}: "
            f"w = {w:10.4f}, loss = {loss:12.4f}"
        )

        w = w - alpha * gradient


# Small steps
gradient_descent(alpha=0.05)

# Useful progress in this example
gradient_descent(alpha=0.4)

# Overshooting and divergence
gradient_descent(alpha=1.1)

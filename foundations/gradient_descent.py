class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        # 設定初始值
        x = init
        
        # 進行指定次數的迭代
        for _ in range(iterations):
            # 計算導數 (Gradient): f'(x) = 2x
            gradient = 2 * x
            
            # 更新規則: x = x - learning_rate * f'(x)
            x = x - learning_rate * gradient
            
        # 將最終結果四捨五入至小數點後 5 位
        return round(x, 5)

# 定义维特比算法
# 求最优路径
def hmm_viterbi(A, B, pi, O):
    T = len(O)
    N = len(A[0])

    delta = [[0] * N for _ in range(T)]  # 定义概率数组
    psi = [[0] * N for _ in range(T)]  # 定义状态数组

    # step1: 初始化
    for i in range(N):
        delta[0][i] = pi[i] * B[i][O[0]]
        psi[0][i] = 0

    # step2: 迭代计算
    for t in range(1, T):
        for i in range(N):
            temp, maxindex = 0, 0
            for j in range(N):
                res = delta[t - 1][j] * A[j][i]
                if res > temp:
                    temp = res
                    maxindex = j

            delta[t][i] = temp * B[i][O[t]]  # delta
            psi[t][i] = maxindex + 1

    # step3: 终止
    p = max(delta[-1])
    for i in range(N):
        if delta[-1][i] == p:
            i_T = i + 1

    # step4：最优路径回溯
    path = [0] * T
    i_t = i_T
    for t in reversed(range(T - 1)):
        i_t = psi[t + 1][i_t - 1]
        path[t] = i_t
    path[-1] = i_T

    return delta, psi, path


A = [[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.2, 0.2, 0.6]]
B = [[0.5, 0.5], [0.4, 0.6], [0.7, 0.3]]
pi = [0.2, 0.3, 0.5]
O = [0, 1, 0, 0, 1, 0, 1, 1]  # 红为 0，白为 1
delta, psi, path = hmm_viterbi(A, B, pi, O)
print("观测概率数组：", delta)
print("状态数组：", psi)  # 状态 1，状态 2，状态 3 （按照课本）
print("概率最大路径：", path)  # 最优路径

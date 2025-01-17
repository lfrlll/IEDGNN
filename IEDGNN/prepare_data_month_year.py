import torch

device=torch.device("cuda:0")
def prepare_data(x, node_emb_u, node_emb_d, T_i_M_emb, T_i_Y_emb):
    if x.dim == 3:
        x = x.unsqueeze(-1)

    time_in_month_feat = T_i_M_emb[(x[:, :, :, 1] * 30).clamp(0, 29).type(torch.LongTensor).to(device)]  # 修改为每月时间特征并限制范围
    time_in_year_feat = T_i_Y_emb[(x[:, :, :, 2] * 12).clamp(0, 11).type(torch.LongTensor).to(device)]  # 修改为每年时间特征并限制范围
    return x, node_emb_u, node_emb_d, time_in_month_feat, time_in_year_feat
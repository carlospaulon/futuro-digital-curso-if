from premium import PlanoPremium
from family import PlanoFamily
from user import Usuario

# Teste do Sistema
if __name__ == "__main__":
    p_premium = PlanoPremium()
    user = Usuario("Marcos Silva", "marcos@email.com", p_premium)
    
    user.gerar_resumo()
    user.processar_assinatura()
    
    # Upgrade para Family
    p_family = PlanoFamily()
    user.alterar_plano(p_family)
    user.processar_assinatura()
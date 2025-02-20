def calculate_savings(income, expenses):
    """Calculate potential savings from income and expenses."""
    total_expenses = sum(expenses.values())
    savings = income - total_expenses
    return savings

def get_investment_recommendation(savings):
    """Generate investment recommendations based on savings amount."""
    recommendations = []
    
    if savings <= 0:
        return ["Você está no negativo. Foque em reduzir despesas antes de pensar em investimentos."]
    
    if savings < 100:
        recommendations = [
            "Comece criando uma reserva de emergência em uma conta poupança",
            "Procure formas de aumentar sua renda e reduzir gastos"
        ]
    elif savings < 500:
        recommendations = [
            "Considere investir em Tesouro Direto",
            "Crie uma reserva de emergência em CDB de liquidez diária",
            "Pesquise sobre fundos de investimento com baixa aplicação inicial"
        ]
    else:
        recommendations = [
            "Diversifique seus investimentos:",
            "- 40% em renda fixa (Tesouro Direto, CDBs)",
            "- 30% em fundos de investimento",
            "- 20% em ações de empresas sólidas",
            "- 10% em criptomoedas (se tiver perfil arrojado)",
            "Considere consultar um assessor financeiro"
        ]
    
    return recommendations

def calculate_expense_percentages(expenses):
    """Calculate percentage of each expense from total."""
    total = sum(expenses.values())
    if total == 0:
        return {}
    return {k: (v/total)*100 for k, v in expenses.items()}

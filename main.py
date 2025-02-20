import streamlit as st
import plotly.express as px
import pandas as pd
from utils import calculate_savings, get_investment_recommendation, calculate_expense_percentages

# Configuração da página
st.set_page_config(
    page_title="Planilha Mágica - Controle Financeiro",
    page_icon="💰",
    layout="wide"
)

# Estilo CSS personalizado
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stAlert {
        padding: 1rem;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.title("🎯 Planilha Mágica - Controle Financeiro")
st.markdown("---")

# Inicialização de estado da sessão
if 'expenses' not in st.session_state:
    st.session_state.expenses = {}

# Seção de Entrada de Dados
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Entrada de Dados")
    
    # Renda mensal
    income = st.number_input(
        "Renda Mensal Total (R$)",
        min_value=0.0,
        value=0.0,
        step=100.0,
        format="%.2f"
    )
    
    # Despesas fixas
    st.markdown("### 📊 Despesas Mensais")
    
    expenses = {}
    expense_types = [
        "Aluguel/Financiamento",
        "Água",
        "Luz",
        "Internet",
        "Alimentação",
        "Transporte",
        "Saúde",
        "Educação",
        "Lazer",
        "Outros"
    ]
    
    for expense in expense_types:
        expenses[expense] = st.number_input(
            f"{expense} (R$)",
            min_value=0.0,
            value=0.0,
            step=10.0,
            format="%.2f"
        )

with col2:
    st.subheader("📈 Resumo Financeiro")
    
    # Cálculo do total de despesas e economia
    total_expenses = sum(expenses.values())
    savings = calculate_savings(income, expenses)
    
    # Exibição dos resultados
    col_metrics1, col_metrics2, col_metrics3 = st.columns(3)
    
    with col_metrics1:
        st.metric(
            label="Renda Total",
            value=f"R$ {income:.2f}",
            delta=None
        )
    
    with col_metrics2:
        st.metric(
            label="Despesas Totais",
            value=f"R$ {total_expenses:.2f}",
            delta=None
        )
    
    with col_metrics3:
        st.metric(
            label="Saldo Mensal",
            value=f"R$ {savings:.2f}",
            delta=f"{'Positivo' if savings >= 0 else 'Negativo'}",
            delta_color="normal" if savings >= 0 else "inverse"
        )
    
    # Gráfico de despesas
    if total_expenses > 0:
        expense_percentages = calculate_expense_percentages(expenses)
        df = pd.DataFrame({
            'Categoria': expenses.keys(),
            'Valor': expenses.values(),
            'Porcentagem': [expense_percentages[k] for k in expenses.keys()]
        })
        
        fig = px.pie(
            df,
            values='Valor',
            names='Categoria',
            title='Distribuição de Despesas',
            hover_data=['Porcentagem'],
            labels={'Porcentagem': 'Porcentagem do Total'}
        )
        st.plotly_chart(fig, use_container_width=True)

# Seção de Recomendações
st.markdown("---")
st.subheader("💡 Recomendações de Investimento")

recommendations = get_investment_recommendation(savings)

for rec in recommendations:
    st.markdown(f"- {rec}")

# Dicas e Alertas
st.markdown("---")
st.subheader("💭 Dicas Financeiras")

if savings < 0:
    st.error("⚠️ Atenção! Suas despesas estão maiores que sua renda. Considere revisar seus gastos.")
elif savings < (income * 0.1):
    st.warning("⚠️ Sua taxa de economia está baixa. Tente economizar pelo menos 10% da sua renda.")
else:
    st.success("✅ Parabéns! Você está conseguindo economizar uma boa parte da sua renda.")

# Dicas gerais
st.info("""
    📌 Dicas para melhorar suas finanças:
    - Tente manter suas despesas fixas em até 50% da sua renda
    - Crie uma reserva de emergência equivalente a 6 meses de despesas
    - Diversifique seus investimentos para reduzir riscos
    - Evite dívidas com juros altos
    - Planeje compras grandes com antecedência
""")

# Rodapé
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Desenvolvido com ❤️ para ajudar no seu controle financeiro</p>
        <p>Use esta planilha mensalmente para acompanhar sua evolução financeira</p>
    </div>
""", unsafe_allow_html=True)

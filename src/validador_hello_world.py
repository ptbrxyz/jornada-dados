from pydantic import BaseModel, Field


class User(BaseModel):
    #name: str = Field(default=123, validate_default=True)

    Organizador: str = Field(..., description="Nome do organizador da campanha.")
    Ano_Mes: str = Field(..., description="Ano e mês no formato 'YYYY-MM'. Ex: '2025-03'.")
    Dia_da_Semana: str = Field(..., description="Dia da semana. Ex: 'Segunda-feira'.")
    Tipo_Dia: str = Field(..., description="Tipo do dia. Ex: 'Trabalho', 'Fim de semana', 'Feriado'.")
    Objetivo: str = Field(..., description="Objetivo da campanha ou do anúncio.")
    Date: date = Field(..., description="Data do evento. Ex: '2025-03-18'.", default_factory=date.today)
    AdSet_name: str = Field(..., description="Nome do conjunto de anúncios.")
    Amount_spent: float = Field(0.0, ge=0, le=1200,0, description="Valor gasto com o anúncio (mínimo=0.0, máximo 600.0).")
    Link_clicks: int = Field(..., description="Quantidade de cliques no link.")
    mpressions: conint(ge=0, le=50782) = Field(..., description="Quantidade de impressões do anúncio, deve estar entre 0 e 50782.")
    Conversions: int = Field(..., description="Número de conversões geradas pelo anúncio.")
    Segmentação: str = Field(..., description="Segmentação do público-alvo do anúncio.")
    Tipo_de_Anúncio: str = Field(..., description="Tipo de anúncio. Ex: 'Imagem', 'Vídeo', 'Carrossel'.")
    Fase: str = Field(..., description="Fase da campanha. Ex: 'Planejamento', 'Execução', 'Finalização'.")

user = User()
print(user)


def atualizar_pontos_usuario(db: Session, user_id: int, pontos_para_adicionar: float):
    # 1. Busca o usuário no banco
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    
    if not db_user:
        return None # Usuário não existe
        
    # 2 Obs: Para diminuir pontos, basta passar um valor negativo na variável
    novo_saldo = float(db_user.points) + pontos_para_adicionar
    
    # Validação: não pode ficar negativo
    if novo_saldo < 0:
        raise ValueError("Saldo insuficiente para a operação.")
        
    # 3. Atualiza o objeto ORM
    db_user.points = novo_saldo
    
    # Atualiza o max_points se o usuário bateu um novo recorde
    if novo_saldo > float(db_user.max_points):
        db_user.max_points = novo_saldo
        
    # 4. Salva no banco de dados
    db.commit()
    db.refresh(db_user)
    
    return db_user
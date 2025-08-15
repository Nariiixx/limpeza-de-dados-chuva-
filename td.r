```{r}
# Limpeza de dados do tempo
#CARREGA OS DADOS
    dados = read.csv("tempo.csv", sep = ";", na.string = c(" ","", NA), stringsAsFactors=FALSE)
    
    # PROCURA OS DADOS NA E DADOS MAIORES QUE 90, ADICONA A MEDIANA NESSES DADOS(COLUNA UMIDADE)
    dados$Umidade[is.na(dados$Umidade)|dados$Umidade >90] <- median(dados$Umidade, na.rm=TRUE)
    
    #ADICONA A MODA NO NAS DA COLUNA VENTO
    dados$Vento[is.na(dados$Vento)] <- FALSE
    
    #ADICIONA A MEDIANA NO NAS DA COLUNA TEMPERATURA, CONVERTE PARA CELSIUS E SUBSTITUI OS VALORES MAIORES QUE 100 POR MEDIANA
    dados$Temperatura[dados$Temperatura > 100] <- median(dados$Temperatura[dados$Temperatura <= 100])
    dados$Temperatura <- (dados$Temperatura - 32) * 5/9
    
    #ADICIONA A MODA NO NAS DA COLUNA APARENCIA
    dados$Aparencia[!dados$Aparencia %in% c("chuva","nublado","sol")]<- "chuva"
    dados
    write.csv(dados, "tempo_limpo.csv", row.names = FALSE)

```
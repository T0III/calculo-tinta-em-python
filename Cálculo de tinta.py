larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
print('*Essa aplicação se baseia na hipotese de 2lt de tinta por m²*')

print('A dimensão da sua parede é de: {}m x {}m'.format(larg, alt))
print('A área total da parede é de: {:.2f}m²'.format(area))
tinta = area / 2
print('A quantidade de tinta para pintar essa parede é de: {:.2f}lt'.format(tinta))




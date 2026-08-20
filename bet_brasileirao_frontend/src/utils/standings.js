// Zonas de classificação do Brasileirão Série A (20 clubes), calculadas a partir
// da posição — o backend não guarda essa classificação, só position/points/etc.
export function standingsZone(position) {
  if (position == null) return null
  if (position <= 4) return 'libertadores'
  if (position <= 6) return 'pre-lib'
  if (position <= 12) return 'sulamericana'
  if (position >= 17) return 'rebaixamento'
  return null
}

// O backend não guarda gols pró/contra, então o aproveitamento é calculado
// a partir de points/playedGames (cada vitória vale 3 pontos).
export function aproveitamento(points, playedGames) {
  if (!playedGames) return '0.0'
  return ((Number(points) / (playedGames * 3)) * 100).toFixed(1)
}

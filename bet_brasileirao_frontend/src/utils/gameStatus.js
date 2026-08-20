// Status vêm da api.football-data.org (sincronizados pelo backend em api/control/api_externa.py)
const LIVE_STATUSES = ['IN_PLAY', 'PAUSED']
const FINISHED_STATUSES = ['FINISHED', 'AWARDED']
// TIMED = agendado com horário confirmado; SCHEDULED = agendado; POSTPONED = adiado (nova data a definir)
const UPCOMING_STATUSES = ['SCHEDULED', 'TIMED', 'POSTPONED']

export function gamePhase(status) {
  if (LIVE_STATUSES.includes(status)) return 'live'
  if (FINISHED_STATUSES.includes(status)) return 'finished'
  if (UPCOMING_STATUSES.includes(status)) return 'upcoming'
  return 'other'
}

// Mesma convenção usada em Game.winner_str e Bet.prediction no backend
export const PREDICTIONS = [
  { key: 'HOME_TEAM', label: 'Casa' },
  { key: 'DRAW', label: 'Empate' },
  { key: 'AWAY_TEAM', label: 'Visitante' }
]

export function predictionLabel(key) {
  return PREDICTIONS.find((p) => p.key === key)?.label ?? key
}

// Erros de validação do Pydantic (422) vêm como um array de { loc, msg, type },
// não como uma string única — sem isso a mensagem apareceria como "[object Object]".
export function extractErrorMessage(err, fallback) {
  const detail = err?.response?.data?.detail
  if (Array.isArray(detail)) {
    return detail.map((d) => d.msg || JSON.stringify(d)).join(' ')
  }
  return detail || fallback
}

function obliczKoszt(noce, osoby, cenaZaOsobeNoc = 120) {
  if (!Number.isInteger(noce) || noce < 1) throw new Error("Podaj liczbę nocy (co najmniej 1)");
  if (!Number.isInteger(osoby) || osoby < 1) throw new Error("Podaj liczbę osób (co najmniej 1)");
  let koszt = noce * osoby * cenaZaOsobeNoc;
  if (noce >= 7) koszt = koszt * 0.9;
  return Math.round(koszt * 100) / 100;
}

document.querySelector("#kalkulator").addEventListener("submit", (e) => {
  e.preventDefault();
  const wynik = document.querySelector("#wynik");
  try {
    const koszt = obliczKoszt(Number(document.querySelector("#noce").value), Number(document.querySelector("#osoby").value));
    wynik.textContent = `Koszt: ${koszt.toFixed(2)} zł`;
  } catch (err) {
    wynik.textContent = err.message;
  }
});

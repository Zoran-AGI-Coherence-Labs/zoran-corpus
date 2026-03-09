```mermaid
flowchart TD
  U[Users] --> PR[PolyResonator<br/>UCB1·EMA·Quorum]
  PR --> GN[GlyphNet<br/>mirror | style | plan]
  PR --> ZDM[ZDM<br/>HardCore + Resonant cache]
  PR --> DM[ΔM11.3<br/>stabilité/rollback]
  GN --> TA[Task Adapters<br/>(Edu | Interaction | Ing)]
  ZDM --> TA
  DM --> TA
  TA --> OBS[Observability<br/>C2PA | SBOM | KPIs]
  OBS --> AE[Aegis Layer<br/>éthique | vigilance | soin (always‑on)]
```
UCB1 : sélection de “spécialistes”/prompts selon upper confidence bound (exploration/exploitation).
Mixer EMA : combinaison des sorties/états par moyenne exponentielle (réduction variance).
Quorum : Self‑Patch Quorum (vote keep/merge/drop) + ΔM11.3 si instabilité.

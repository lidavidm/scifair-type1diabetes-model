Bifurcation diagram:

- X axis is inversely proportional to the level of pancreatic beta cells
  remaining and directly proportional to δₚ, rate at which immune system
  clears dead cells
- Y axis is number of T cells, which roughly determines how quickly
  pancreatic cells die
- At (0, 0) all beta cells alive.
- Killing beta cells leads to fluctuations at δₚ=0.5707.
- Solid lines/green dots: if you start on or near that point, you stay there
- Dashed lines/red circles: if you don't start on that point, you evolve to
  some other equilibrium
- Note: cell levels are estimates
- Reference: Mahaffy 2007

Combined diagram, 0.1 to 2:

- Minor fluctuations begin before the level of beta cells has reached the
  expected critical level, i.e. the cyclic effect originally described
  applies to levels below the original, though it may not be noticeable,
  especially given the *large* error bars in the original experiments
  (ref. Mareé)

Combined diagram, 0.1 to 2 (1000 days):

- If the beta cells die slowly enough, no fluctuations start until well
  after the expected point, and the magnitude increases much more quickly
- These fluctuations may occur even after it would be expected that they
  stop
- Causes of slow death: regeneration, medication
  - Future research: implement regeneration in the model

Combined diagram, 0.5 to 2.3:

- Starting from near the critical point leads to the expected behavior

Combined diagram, 2 to 0.1:

- For someone already in the region where diabetic symptoms occur,
  regenerating beta cells still causes an immune response (though in this
  case, the regeneration outweighs the immune response)
- In terms of reversing the effects on an individual who has undergone the
  effects of the 0.1 to 2 variation: regeneration must be able to outpace
  the immune response; immune response is also more severe
- Notably, response does not track the steady state as it is unstable
- Normal δₚ is high, so decreasing it (in diabetic mice it is unusually low)
  triggers an immune response!

Slowly varying parameter (forward):

- At high clearance rates, killing beta cells doesn't trigger a response
  because not enough die to create enough peptide to set off the immune
  system
- High rates are normal; making them higher doesn't cause any adverse
  effects, even if the immune system is already somewhat reactive to beta
  cells (ref. Mahaffy)

Slowly varying parameter (backward):

- "Regenerating" the beta cells prevents fluctuation; at a high clearance
  rate, not enough die to cause a spike (not much dead cell peptide is left
  to trigger a response)

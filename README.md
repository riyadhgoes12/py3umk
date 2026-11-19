# Molecular Beam Characterization by REMPI UV Pulse Laser

<<<<<<< HEAD
My project is about Molecular Spectroscopy by UV pulse laser. We provides ionized photon as a detection of next level jump from elecron-photon exchange. Resonance-Enhanced Multi-Photon Ionization (REMPI) spectroscopy provides a powerful approach for sensitive quantum state-selective detection of molecules
I will add the desc in.
=======
Resonance-Enhanced Multi-Photon Ionization (REMPI) spectroscopy provides a powerful approach for sensitive quantum state-selective detection of molecules. In particular, hydrogen and its isotopologues. We investigate state-selective ionization of $\text{H}_2$ using UV laser pulses near 202 nm and 211 nm, targeting lines such as Q(1) 1–0 to access ground and excited vibrational states. In our approach, we are developing a detection system essential for performing high-resolution rovibrational spectroscopy of trapped hydrogen molecules.

Below is the schematic of generating $[2+1]$ REMPI in this PhD Project:
>>>>>>> 1da649d (docs(readme): fully describe)

![Schematic of Molecular Beam Characterization](schematic.png)

# REMPI spectral data analysys

## What is this software for

Implement a phyton code for data processing and spectral analysis toolkit for high-resolution $[2+1]$ REMPI laser spectroscopy of molecular hydrogen ($\text{H}_2$). It takes large batches of raw oscilloscope `.txt` recordings where each file contains of wavelength stepped in time-domain points and automates pulse extraction, baseline normalization, spectral integration, and Gaussian/Lorentzian lineshape fitting to extract Full Width at Half Maximum ($\text{FWHM}$) across varying $\text{H}_2$ pressures and UV laser powers.

---

## Processing Pipeline

1. **Batch Ingestion & Sorting:** Reads multirow oscilloscope `.txt` files and sorts individual pulses.
2. **Baseline Subtraction:** Removes DC baseline offset per trace and normalizes pulse amplitudes prior to integration.
3. **Pulse Integration:** Integrates the normalized pulse signal over the arrival time window at each wavelength step to construct the $[2+1]$ REMPI spectrum:
   $$I(\lambda) = \int_{t_1}^{t_2} S_{\text{norm}}(t, \lambda) \, dt$$
4. **Lineshape Fitting & FWHM Extraction:** Isolates the narrowest spectral transition and fits both Gaussian and Lorentzian profiles to determine pressure broadening and AC Stark / power broadening:
   - **Gaussian profile:**
     $$G(\lambda; A, \lambda_0, \sigma) = A \exp\left( -\frac{(\lambda - \lambda_0)^2}{2\sigma^2} \right), \quad \text{FWHM}_G = 2\sqrt{2\ln 2}\,\sigma$$
   - **Lorentzian profile:**
     $$L(\lambda; A, \lambda_0, \gamma) = \frac{A}{\pi} \frac{\gamma}{(\lambda - \lambda_0)^2 + \gamma^2}, \quad \text{FWHM}_L = 2\gamma$$
5. **Comparative Parameter Analysis:** Compares extracted $\text{FWHM}$ and line shifts across datasets recorded at different $\text{H}_2$ chamber pressures and UV pulse powers.

---

## Installation

Clone the repository and install the required scientific Python dependencies (`numpy`, `scipy`, `matplotlib`):

```bash
git clone [https://github.com/riyadhgoes12/py3umk.git](https://github.com/riyadhgoes12/py3umk.git)
cd py3umk
pip install numpy scipy matplotlib
```





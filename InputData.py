
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1         # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03
ADD_BACKGROUND_MORT = True #if background mortality should be added

# transition matrices
TRANS_MATRIX1 = [
    [0.0,  0.1625,   0.6694,    0.1681],        # Well
    [0,    0.0003507,    0.99928,    0.000362], # Stroke
    [0,    0.09577,   0.88113,   0.0231],       # Post-Stroke
    [0.0,  0.0,    0.0,    1.0],                # Dead
    ]

#with 25% decrease and 5% increase
TRANS_MATRIX = [
    [0.0,  0.1541,   0.6694,    0.1765],        # Well
    [0,    0.0003507,    0.99928,    0.000362], # Stroke
    [0,    0.0718,   0.9051,   0.0231],         # Post-Stroke
    [0.0,  0.0,    0.0,    1.0],                # Dead
    ]

# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.65
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = 1.05

#annual health utility of each health state
HEALTH_UTILITY = [
    1,  # well
    0.2,  # stroke ONLY WHEN THE CYCLE LENGTH IS 1 YEAR
    0.9,  # post-stroke
    0  # dead
]

#annual cost of each health state
HEALTH_COST = [
    0,
    5000,  # stroke
    200,  # post-stroke /yeear
    0
]

Anticoag_COST = 750

#annual probability of background mortality (number per year per 1,000 population)
ANNUAL_PROB_BACKGROUND_MORT = 17.638 / 1000
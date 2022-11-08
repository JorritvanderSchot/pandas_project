import argparse
from . import climate

def climate_calculation():
    """Entry point for the climate_calculation function"""
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--station",
        required=True,
        type=float,
        help="Select a station from the dataset by station number (Graz = 30)."
    )
    parser.add_argument(
        "--hotorfrost",
        required=False,
        action="store_true",
        help="Do you want to calculate 'hot' or 'frost' days? Select your desired option."
    )
    parser.add_argument(
        "--plot",
        required=False,
        action="store_true",
        help="True or False. Do you want to plot the annual trend?"
    )
    parser.add_argument(
        "--begin",
        required=False,
        action="store_true",
        help="Beginning of the period you want to analyze."
    )
    parser.add_argument(
        "--end",
        required=False,
        action="store_true",
        help="End of the period you want to analyze."
    )
    parser.add_argument(
        "--threshold",
        required=False,
        action="store_true",
        help="Threshold value for hot or frostdays.",
    ) 
    parser.add_argument(
        "--variable",
        required=False,
        action="store_true",
        help="Variable to plot (t, tmin or tmax)."
    )

    args = parser.parse_args()

    climate.hotfrostdays(args.station,args.hotorfrost, args.plot, args.begin, args.end, args.threshold, args.df)
    if args.variable:
        climate.monthly_T_anomalies(args.variable)
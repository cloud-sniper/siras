
from modules.smokers.SGopenSmoker import SGopenSmoker
from modules.smokers.PanAuthSmoker import PanAuthSmoker
from modules.smokers.AWSadminSmoker import AWSadminSmoker
from modules.smokers.awsConsoleAuthSmoker import awsConsoleAuthSmoker
from modules.smokers.CTrailSmoker import CTrailSmoker
from modules.smokers.S3PublicSmoker import S3PublicSmoker
from modules.smokers.EBSPublicSmoker import EBSPublicSmoker
from modules.smokers.test_logger import test_message
from modules.welcome import home
from modules.logs import droid_logger, droid_s3_logger

import argparse


def main(args):
    if args.get('bucket') == True:
        droid_s3_logger('cloud-droid')
        if args.get('smoker') == 'test':
            test_message()
        if args.get('smoker') == 'sg':
            SGopenSmoker()
        if args.get('smoker') == 'pa':
            PanAuthSmoker()
        if args.get('smoker') == 'au':
            AWSadminSmoker()
        if args.get('smoker') == 'aca':
            awsConsoleAuthSmoker()
        if args.get('smoker') == 'ctr':
            CTrailSmoker()
        if args.get('smoker') == 's3p':
            S3PublicSmoker()
        if args.get('smoker') == 'esb':
            EBSPublicSmoker()
        if args.get('smoker') == 'all':
            SGopenSmoker()
            PanAuthSmoker()
            AWSadminSmoker()
            awsConsoleAuthSmoker()
            CTrailSmoker()
            S3PublicSmoker()
            EBSPublicSmoker()
    else:
        droid_logger('droid')
        if args.get('smoker') == 'test':
            test_message()
        if args.get('smoker') == 'sg':
            SGopenSmoker()
        if args.get('smoker') == 'pa':
            PanAuthSmoker()
        if args.get('smoker') == 'au':
            AWSadminSmoker()
        if args.get('smoker') == 'aca':
            awsConsoleAuthSmoker()
        if args.get('smoker') == 'ctr':
            CTrailSmoker()
        if args.get('smoker') == 's3p':
            S3PublicSmoker()
        if args.get('smoker') == 'esb':
            EBSPublicSmoker()
        if args.get('smoker') == 'all':
            SGopenSmoker()
            PanAuthSmoker()
            AWSadminSmoker()
            awsConsoleAuthSmoker()
            CTrailSmoker()
            S3PublicSmoker()
            EBSPublicSmoker()


if __name__ == '__main__':
    home()
    print('Cloud Incident and Response Simulations. Lets you perform tabletop exercises, which measures the effectiveness in defining the incident response plan. It works as a red/purple-team-as-code, which checks if your security posture is adequate.\n\n https://github.com/cloud-sniper/cloud-droid.\n\n')
    droid_parser = argparse.ArgumentParser()
    droid_parser.version = 'version: 2.0 - https://github.com/cloud-sniper/cloud-droid'
    droid_parser.add_argument(
        '-s', help='smoker to run', dest='smoker', type=str, required=True)
    droid_parser.add_argument(
        '-b', help='save the results into a bucket', dest='bucket', type=bool, required=False)
    args = droid_parser.parse_args()
    event_map = {'smoker': args.smoker, 'bucket': args.bucket}
    main(event_map)

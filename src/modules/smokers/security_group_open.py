#!/usr/bin/python

import boto3
from botocore.exceptions import ClientError

from smoker import BaseSmoker


# Smoker for open security group

class SecGroupOpenSmoker(BaseSmoker):

    def sell(self):
        description = "Cloud Droid smoke security group " + self.iso_now_time
        name = "cloud_droid_smoke_group"
        ec2 = boto3.client("ec2")
        response = ec2.describe_vpcs()
        vpc_id = response.get("Vpcs", [{}])[0].get("VpcId", "")
        try:
            response = ec2.create_security_group(GroupName=name,
                                                 Description=description,
                                                 VpcId=vpc_id)
            security_group_id = response["GroupId"]
            self.logger.info(f"Security Group Created {security_group_id} "
                             f"in vpc {vpc_id}")

            data = ec2.authorize_security_group_ingress(
                GroupId=security_group_id,
                IpPermissions=[
                    {
                        "IpProtocol": "tcp",
                        "FromPort": 80,
                        "ToPort": 80,
                        "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
                    },
                    {
                        "IpProtocol": "tcp",
                        "FromPort": 22,
                        "ToPort": 22,
                        "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
                    }
                ], )
            self.logger.info("Successfully Set %s" % data)
        except ClientError as e:
            self.logger.error(e)
        try:
            response = ec2.delete_security_group(GroupId=security_group_id)
            self.logger.info("Security Group Deleted")
        except ClientError as e:
            self.logger.error(e)

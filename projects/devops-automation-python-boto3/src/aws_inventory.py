"""Safe, read-only AWS inventory example using Boto3."""
import boto3


def list_ec2_instances(region: str) -> None:
    ec2 = boto3.client("ec2", region_name=region)
    response = ec2.describe_instances()
    for reservation in response.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            print({
                "id": instance.get("InstanceId"),
                "state": instance.get("State", {}).get("Name"),
                "type": instance.get("InstanceType"),
                "private_ip": instance.get("PrivateIpAddress"),
            })


if __name__ == "__main__":
    list_ec2_instances("ap-south-1")

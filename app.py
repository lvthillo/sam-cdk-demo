#!/usr/bin/env python3

from aws_cdk import core

from sam_cdk_demo.sam_cdk_demo_stack import SamCdkDemoStack


app = core.App()
SamCdkDemoStack(app, "sam-cdk-demo")

app.synth()

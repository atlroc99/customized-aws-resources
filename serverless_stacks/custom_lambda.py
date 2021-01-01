from aws_cdk import core
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_logs as _logs

class CustomLambdaStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # create serverless event processor using lambda ):

        # read the function content ):
        lambda_function_code = ''
        try:
            with open('serverless_stacks/lambda_src/konestone_processor.py', mode='r') as f:
                print("READ FUNCTION")
                lambda_function_code = f.read()
                print("FINISH READING ", lambda_function_code)
        except OSError:
            print('Unable to read the file and the content of the file')

        _code = _lambda.InlineCode(lambda_function_code)
        # create a lambda function with the method content/ body we retrieved
        konestone_function = _lambda.Function(self,
                         id="firstLambdaFunctionID",
                         function_name="konstone_function",
                         runtime=_lambda.Runtime.PYTHON_3_7,
                         handler="index.lambda_handler",  # which method to execute when lambda function is called
                         code=_code,
                         timeout=core.Duration.seconds(3),
                         reserved_concurrent_executions=1,
                         environment={
                             'LOG_LEVEL': 'INFO'
                         })

        #create an attach log group for the above lambda function. If this stack is delete the log group will also be deleted
        konestone_lg = _logs.LogGroup(self,
                                      id="konestone_lambda_log_group",
                                      log_group_name=f"/aws/lambda/{konestone_function.function_name}",
                                      removal_policy=core.RemovalPolicy.DESTROY)


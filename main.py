from config.slack_config import slack_config
from slack.slack_app import SlackApp


def main():
    # llm_client = OpenAIClient(open_ai_config.api_key, OpenAIModel.gpt_4o_mini) need to define here and uses di
    slack_app = SlackApp(slack_config)
    slack_app.start_slack_app()


if __name__ == "__main__":
    main()

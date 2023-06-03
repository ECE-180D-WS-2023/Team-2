using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using M2MqttUnity;
using uPLibrary.Networking.M2Mqtt;
using uPLibrary.Networking.M2Mqtt.Messages;
using UnityEngine.Windows.Speech;

public class chat : MonoBehaviour
{
    bool multiplayerWorld = false;
    bool complete = false;
    private DictationRecognizer dictationRecognizer;

    MqttClient client = new MqttClient("mqtt.eclipseprojects.io");

    void Start()
    {
        string[] mqtt_topic = { "Team-2/Digimon/players/#" };
        byte[] mqtt_qosLevels = { MqttMsgBase.QOS_LEVEL_AT_MOST_ONCE };

        client.MqttMsgPublishReceived += client_MqttMsgPublishReceived;
        client.Connect("");
        client.Subscribe(mqtt_topic, mqtt_qosLevels);
        Debug.Log("mqtt connected");
    }

    void client_MqttMsgPublishReceived(object sender, MqttMsgPublishEventArgs e)
    {
        if (multiplayerWorld)
        {
            if (e.Topic == "Team-2/Digimon/players/player1/chat")
            {
                Debug.Log("Player 1: " + System.Text.Encoding.UTF8.GetString(e.Message));
            }
            else if (e.Topic == "Team-2/Digimon/players/player2/chat")
            {
                Debug.Log("Player 2: " + System.Text.Encoding.UTF8.GetString(e.Message));
            }
        }
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.U))
        {
            multiplayerWorld = true;
            //Debug.Log("multi chat");
        }
        else if (Input.GetKeyDown(KeyCode.Escape))
        {
            multiplayerWorld = false;
            //Debug.Log("exit multi chat");
        }
        else if (Input.GetKeyDown(KeyCode.V))
        {
            complete = false;
            StartCoroutine(startChatting());
        }
    }

    private void DictationRecognizer_DictationResult(string text, ConfidenceLevel confidence)
    {
        client.Publish("Team-2/Digimon/players/player2/chat", System.Text.Encoding.UTF8.GetBytes(text));
        complete = true;
        //Debug.Log("send");
    }

    public void DictationRecognizer_DictationComplete(DictationCompletionCause cause)
    {
        //Debug.Log("complete");
    }

    IEnumerator startChatting()
    {
        dictationRecognizer = new DictationRecognizer();
        dictationRecognizer.DictationResult += DictationRecognizer_DictationResult;
        dictationRecognizer.DictationComplete += DictationRecognizer_DictationComplete;
        dictationRecognizer.Start();
        // Debug.Log("chat speech started");

        yield return new WaitWhile(() => (Input.GetKey(KeyCode.V)) && complete != true);
        Debug.Log("let go of V and complete");
        //dictationRecognizer.DictationResult -= DictationRecognizer_DictationResult;
        dictationRecognizer.Stop();
        //dictationRecognizer.Dispose();
    }
}
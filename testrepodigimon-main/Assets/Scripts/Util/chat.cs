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
            // print message to chatbox

        }
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.U))
        {
            multiplayerWorld = true;
        }
        else if (Input.GetKeyDown(KeyCode.Escape))
        {
            multiplayerWorld = false;
        }

        if (Input.GetKeyDown(KeyCode.V))
        {
            dictationRecognizer = new DictationRecognizer();
            dictationRecognizer.DictationResult += DictationRecognizer_DictationResult;
        }
    }

    private void DictationRecognizer_DictationResult(string text, ConfidenceLevel confidence)
    {
        client.Publish("Team-2/Digimon/players/player1/chat", System.Text.Encoding.UTF8.GetBytes(text));
    }
}

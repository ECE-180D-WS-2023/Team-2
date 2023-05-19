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

        dictationRecognizer = new DictationRecognizer();
        dictationRecognizer.DictationResult += DictationRecognizer_DictationResult;
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
            Debug.Log("multii chat");
        }
        else if (Input.GetKeyDown(KeyCode.Escape))
        {
            multiplayerWorld = false;
        }
        else if (Input.GetKey(KeyCode.V))
        {
            StartCoroutine(speechCall());
        }
        else if (Input.GetKeyUp(KeyCode.V))
        {
            new WaitForSeconds(2);
            dictationRecognizer.DictationResult -= DictationRecognizer_DictationResult;
            dictationRecognizer.Stop();
            dictationRecognizer.Dispose();
        }
    }

    private void DictationRecognizer_DictationResult(string text, ConfidenceLevel confidence)
    {
        client.Publish("Team-2/Digimon/players/player1/chat", System.Text.Encoding.UTF8.GetBytes(text));
        Debug.Log("Player 1: " + text);
    }

    IEnumerator speechCall()
    {
        dictationRecognizer.Start();
        Debug.Log("chat speech started");
        while (!Input.GetKeyUp(KeyCode.V))
        {

        }
        yield return new WaitForSeconds(1);
    }

}

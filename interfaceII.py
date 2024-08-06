import streamlit as st
import deploy

st.set_page_config(
    page_title="IoMT Security Simulator",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Simulate Attack", "Preemptive Analysis"])

preemptive_prompts = [
    "My insulin pump has been working fine, but lately, I've noticed Traffic was observed with the following characteristics: Header length of 36043.6 bytes, using the 6.0 protocol. The connection duration was 64.0 seconds with a rate of 1.3366900608925942 bytes per second, and source rate 1.3366900608925942 bytes per second. The packet contains 0.0 SYN flags, 0.0 RST flags, and 1.0 ACK flags. The SYN packet count is 0.0, FIN packet count is 0.0, and RST packet count is 466.5. TCP traffic is present (1.0), UDP traffic is present (0.0), ICMP traffic is present (0.0), IPv traffic is present (1.0), and LLC traffic is present (1.0). Statistical measures include a total sum of 413.7, minimum value of 66.0, maximum value of 85.8, average of 74.4020238095238, standard deviation of 9.176143913768222, total size of 76.3 bytes, inter-arrival time of 7.359981536865234e-05 microseconds, number of packets 5.5, magnitude 12.1959306758997, radius 12.97702717313835, covariance 93.66396697845803, variance 0.9, and weight 38.5.. I'm not sure if it's just a glitch, but it's making me anxious. What should I do?"
]

attack_prompts = [
    "Spoofing",
    "DDoS",
    "DoS",
    "MQTT",
    "Recon"
]


def display_home():
    st.title("IoMT Security Simulator")
    st.write(
        """
        Welcome to the IoMT Security Simulator! This tool helps simulate attacks on IoMT devices and provides
        preemptive analysis to mitigate potential security threats.
        Use the navigation on the left to explore different functionalities.
        """
    )


def simulate_attack():
    st.title("Simulate Attack")
    st.write("Enter the kind of attack you would like to simulate.")

    st.write("### Sample Prompts")
    selected_prompt = st.radio("Choose a sample prompt to use:", attack_prompts)


    if st.button("Use Sample Prompt"):
        st.session_state.attack_description = selected_prompt

    attack_description = st.text_area(
        "Attack Type",
        value=st.session_state.get('attack_description', ''),
        placeholder="Describe the attack scenario here..."
    )

    if st.button("Simulate"):
        if attack_description.strip():  # Check if the text area is not empty
            try:
                simulation_result = deploy.simulate(attack_description)
                st.write("### Simulation Steps")
                st.write(simulation_result)
            except Exception as e:
                st.error(f"An error occurred during simulation: {e}")
        else:
            st.warning("Please provide a description of the attack.")


def preemptive_analysis():
    st.title("Preemptive Analysis")
    st.write("Please describe the problems you're experiencing with IoMT devices in your network, including the specific devices (e.g., heart monitors, insulin pumps) and issues (e.g., connectivity problems, data inaccuracies). Mention how often these problems occur and any patterns. Explain the impact on operations and patient care, and outline any steps you've already taken to address them.")

    st.write("### Sample Prompts")
    selected_prompt = st.radio("Choose a sample prompt to use:", preemptive_prompts)

    if st.button("Use Sample Prompt", key="preemptive_sample"):
        st.session_state.analysis_description = selected_prompt

    st.write("### Please describe any unusual activity or performance issues you have noticed with your IoMT device.")

    analysis_description = st.text_area(
        "Analysis Description",
        value=st.session_state.get('analysis_description', ''),
        placeholder="Describe the analysis scenario here..."
    )

    if st.button("Analyze"):
        if analysis_description.strip():  # Check if the text area is not empty
            try:
                analysis_result = deploy.mitigate(analysis_description)
                st.write("### Analysis Result")
                st.write(analysis_result)
            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")
        else:
            st.warning("Please provide a description for analysis.")


if page == "Home":
    display_home()
elif page == "Simulate Attack":
    simulate_attack()
elif page == "Preemptive Analysis":
    preemptive_analysis()

if __name__ == "__main__":
    st.sidebar.write("Select a page to begin.")

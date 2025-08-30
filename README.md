# Movie Recommendation System 🎬
A simple **Movie Recommendation System** built using Python, NLP, and machine learning techniques. The system suggests movies similar to a given movie using **text-based features** like movie overviews and plots.
---
## **Live Demo**
Check out the interactive demo here: 🔗 [Movie Recommendation System - Streamlit App](https://movierecommend-8ayh6vbuorbh7uytq6bgse.streamlit.app/)
---
## **GitHub Repository**
All code is available here: 🔗 [GitHub - Movie Recommendation System](https://github.com/Animesh-Samantaray/movieRecommend.git)
---
## **Project Overview**
This project demonstrates how to build a **movie recommendation system** from scratch using Python and NLP.
### **Key Steps**
**✨ Data:** Collected a rich movie dataset from **Kaggle** containing movie titles, plots, genres, and more.  
**🧹 Preprocessing:** Cleaned text data by removing stopwords and performing **stemming** using **NLTK**.  
**📊 Vectorization:** Converted movie plots into numeric vectors using **CountVectorizer**.  
**🎯 Recommendation:** Calculated **cosine similarity** between movie plots to find the **10 most similar movies**.  
**💻 Deployment:** Deployed the system as an interactive web app using **Streamlit**. Users can enter a movie and get instant recommendations.
---
## **Folder Structure**
```
movieRecommend/
├── app.py                 # Streamlit app
├── model.pkl              # Trained model or data vectors (if saved)
├── movies.csv             # Movie dataset
├── preprocessing.py       # Text preprocessing functions
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
```
---
## **Installation & Usage**
1. Clone the repository:
```bash
git clone https://github.com/Animesh-Samantaray/movieRecommend.git
cd movieRecommend
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the Streamlit app:
```bash
streamlit run app.py
```
4. Enter a movie title in the input box to see **recommended movies**.
---
## **Future Improvements**
- Integrate **user ratings** for collaborative filtering recommendations.  
- Use **TF-IDF or embeddings** for better text similarity.  
- Enhance **UI/UX** of the Streamlit app.
---
## **Author**
**Animesh Samantaray** – Computer Science Student & ML Enthusiast
---
## **License**
This project is licensed under the **MIT License** – see [LICENSE](LICENSE) for details.

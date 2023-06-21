# source: jason-leung from unsplash
logo = "./jason-leung-1DjbGRDh7-E-unsplash.jpg"
image = Image.open(logo)
img_logo = np.array(image)
img_shape = (int(0.05*img_logo.shape[1]),int(0.05*img_logo.shape[0]))
img_logo = cv.resize(img_logo, img_shape, interpolation=cv.INTER_AREA)
st.image(img_logo)
'''
# Prototype App for Image Classification
'''

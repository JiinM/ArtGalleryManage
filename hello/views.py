from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Prefetch
from .models import Exhibits, Reservations, Artists, Visitors
from .forms import ExhibitForm

# Function to list all exhibits
def exhibit_list(request):
    print('begin exhibit list')
    exhibits = Exhibits.objects.select_related('artist').prefetch_related('reservations__visitor').all()
    for exhibit in exhibits:
        print(f"Exhibit: {exhibit.title}")
        for res in exhibit.reservations.all():
            print(f"   Reservation: Visitor {res.visitor.name}, Status: {res.status}")
    return render(request, 'exhibits/list.html', {'exhibits': exhibits})


# Function to create a new exhibit
def exhibit_create(request):
    if request.method == 'POST':
        artist_id = request.POST.get('artist')
        other_artist_name = request.POST.get('other_artist_name')
        other_artist_country = request.POST.get('other_artist_country')

        if artist_id == 'other' and other_artist_name and other_artist_country:
            # Create artist with both name and country
            new_artist = Artists.objects.create(name=other_artist_name, country=other_artist_country)
            # Update POST data with new artist id
            post_data = request.POST.copy()
            post_data['artist'] = new_artist.id
            form = ExhibitForm(post_data)
        else:
            form = ExhibitForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('exhibit_list')
    else:
        form = ExhibitForm()

    return render(request, 'exhibits/form.html', {'form': form})



# Function to update an existing exhibit
def exhibit_update(request, pk):
    exhibit = get_object_or_404(Exhibits, pk=pk)

    if request.method == 'POST':
        artist_id = request.POST.get('artist')
        other_artist_name = request.POST.get('other_artist_name')
        other_artist_country = request.POST.get('other_artist_country')

        if artist_id == 'other' and other_artist_name and other_artist_country:
            new_artist = Artists.objects.create(name=other_artist_name, country=other_artist_country)
            post_data = request.POST.copy()
            post_data['artist'] = new_artist.id
            form = ExhibitForm(post_data, instance=exhibit)
        else:
            form = ExhibitForm(request.POST, instance=exhibit)

        if form.is_valid():
            form.save()
            return redirect('exhibit_list')
    else:
        form = ExhibitForm(instance=exhibit)

    return render(request, 'exhibits/form.html', {'form': form})



# Function to delete an exhibit
def exhibit_delete(request, pk):
    exhibit = get_object_or_404(Exhibits, pk=pk)
    exhibit.delete()
    return redirect('exhibit_list')

def index(request):
    return render(request, 'index.html')
